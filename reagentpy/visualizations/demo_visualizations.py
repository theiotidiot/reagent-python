import sys
from typing import Optional
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from reagentpy.clients.enrichments import EnrichmentsClient
from reagentpy.clients.composite_scores import CompositeClient
from reagentpy.clients.repo import RepoClient
from datetime import datetime, timedelta
from reagentpy.ReagentClient import ReagentClient


class DemoVisClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def to_title_case(self, start_string: str) -> str:
        return start_string.replace("_", " ").title()
    
    def within_three_months(self, raw_target_date):
        target_date = datetime.strptime(raw_target_date, "%Y-%m-%d")
        current_date = datetime.now()
        three_months_ago = current_date - timedelta(days=90)
        return target_date >= three_months_ago


    def wordcloud(self, repo: Optional[str] = None):
        data = RepoClient().email_domains(repo).dict()

        word_freq_dict = {item['domain']: item['instances'] for item in data}
        
        wc = WordCloud(
            width=1600,
            height=600,
            background_color="white",
            stopwords=None,
            min_font_size=10,
        ).generate_from_frequencies(word_freq_dict)
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wc)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()


    def print_hygiene_summary(self, repo: str):
        data = RepoClient().hygiene_summary(repo).dict()[0]

        name_and_desc = ("\033[1mRepository Overview:\033[0m \033[94m"
            + repo + "\033[0m\n"
            "\033[1mDescription:\033[0m " + data["description"] + "\n")
        contribution_pattern = ("\033[1mTotal Contributors:\033[0m "
            + str(data["total_contributors"])
            + ", spanning across "
            + str(data["total_timezones"])
            + " timezones, indicating a "
            + ("personal project" if data["total_contributors"] == 1 else "") 
            + ("research" if data["total_contributors"] <= 20 else "")
            + ("corporate" if data["total_contributors"] > 20 and data["total_timezones"] <= 2 else "")
            + ("global" if data["total_contributors"] > 20 and data["total_timezones"] > 3 else "")
            + " contribution pattern.\n")
        fork_count = ("\033[1mFork Count:\033[0m "
            + str(data["forks"])
            + ", showcasing "
            + ("a lack of" if data["forks"] == 1 else "")
            + ("a small amount of" if data["forks"] <= 10 else "")
            + ("a moderate amount of" if data["forks"] <= 100 else "")
            + ("a significant amount of" if data["forks"] <= 1000 else "")
            + ("immense" if data["forks"] > 1000 else "")
            + " community engagement and interest.\n")
        license_presence = ("\033[1mLicense Presence:\033[0m "
            + ("Present" if data["has_license"] else "Not Found")
            + ", a necessary aspect of open source contribution.\n")
        readme_presence = ("\033[1mReadme Presence:\033[0m "
            + ("Present" if data["has_readme"] else "Not Found")
            + ", vital for repository documentation.\n")
        recent_commit = ("\033[1mRecent Activity:\033[0m "
            + "The repository was last active on " + str(data["last_activity_at"]) + ", indicating a"
            + ("n active" if self.within_three_months(data["last_activity_at"]) else " stale")
            + " status.")
        print(name_and_desc + contribution_pattern + fork_count + license_presence + readme_presence + recent_commit)


    def create_out_of_ten_chart(self, repo: Optional[str] = None):

        data = EnrichmentsClient().threat_score(repo).dict()
        if len(data) != 1:
            raise ValueError("Expected a single dictionary of values, but got multiple.")
        values = data[0]

        # Create and display charts for each metric
        for raw_title in values:

            score = values[raw_title]

            title = f"{raw_title.replace('_', ' ').title()} out of Ten"

            fig, ax = plt.subplots(figsize=(10, 1.5))

            ax.barh(y=0, width=10, color="skyblue", align="center")
            # Create the foreground bar (actual score)
            ax.barh(y=0, width=score, color="orange", align="center")

            ax.set_xlim(0, 10)
            ax.set_yticks([])
            ax.set_title(title)

            if score == 10:
                ax.text(score, 0, "", ha="left", va="center")
            else:
                ax.text(score, 0, f"{score:.2f}", ha="left", va="center")

            plt.tight_layout()
            plt.show()


    def nationality_pie_chart(self, country_counts, repo):
        # Prepare data for the pie chart
        labels = list(country_counts.countries.keys())
        sizes = list(country_counts.countries.values())

        # Plotting the pie chart
        plt.figure(figsize=(10, 7))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"National Contributions to Repo: {repo}")
        plt.axis("equal")  # Equal aspect ratio ensures that pie chart is drawn as a circle.

        # Show the pie chart
        plt.show()


    def nationality_horizontal_bar_chart(self, country_counts, repo):
        # Prepare data for the bar chart
        labels = list(country_counts.countries.keys())
        sizes = list(country_counts.countries.values())

        # Calculate the cumulative sum of sizes to position the labels
        cumulative_sizes = [
            sum(sizes[: i + 1]) / sum(sizes) * 100 for i in range(len(sizes))
        ]
        cumulative_sizes.insert(
            0, 0
        )  # Add a zero at the start for the first label position

        # Plotting the bar chart
        fig, ax = plt.subplots(figsize=(14, 1))

        # Create horizontal bars
        bar_widths = [size / sum(sizes) * 100 for size in sizes]
        colors = plt.get_cmap("tab10")(range(len(sizes)))  # Generate distinct colors

        bars = ax.barh(
            y=0, width=bar_widths, left=cumulative_sizes[:-1], color=colors, align="center"
        )

        # Add labels inside the bands
        for i, bar in enumerate(bars):
            width = bar.get_width()
            x_position = bar.get_x() + width / 2
            ax.text(
                x_position,
                bar.get_y(),
                f"{labels[i]}: {sizes[i]}%",
                ha="center",
                va="bottom",
                color="white",
                fontweight="bold",
            )

        ax.set_yticks([])
        ax.set_xlim(0, 100)

        # Adding titles and labels
        ax.set_title(f"National Contributions to Repo: {repo}")
        ax.set_xlabel("Contributions (%)")

        # Show the bar chart
        plt.show()


    def hibp_pie_chart(self, repo: str, include_unbreached: Optional[bool] = False):
        try:
            hibp_counts = EnrichmentsClient().hibp_for_visualizations(repo).dict()

        except Exception as e:
            print("An error occurred: ", e, file=sys.stderr)
            raise e

        # Prepare data for the pie chart
        labels = []
        sizes = []
        for value in hibp_counts:
            if include_unbreached and (value["hibp_item"] == "Unbreached" or value["hibp_item"] == ""):
                continue
            labels.append(value["hibp_item"])
            sizes.append(value["item_count"])

        # Plotting the pie chart
        plt.figure(figsize=(14, 11))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"Data Breaches in: {self.to_title_case(repo)}")
        plt.axis("equal")  # Equal aspect ratio ensures that pie chart is drawn as a circle.

        # Show the pie chart
        plt.show()


    def political_chart(self, country_counts, repo):
        # Define the countries that fall under "theirs"
        their_countries = [
            "CN",
            "RU",
            "AF",
            "CU",
            "SY",
            "IR",
            "BY",
            "ER",
            "ML",
            "MM",
            "NI",
            "NE",
            "KP",
            "VE",
            "ZW",
        ]

        other_size = sum(
            value for key, value in country_counts.countries.items() if key == "Unspecified"
        )
        ours_size = sum(
            value
            for key, value in country_counts.countries.items()
            if key != "Unspecified" and key not in their_countries
        )
        theirs_size = sum(
            value
            for key, value in country_counts.countries.items()
            if key != "Unspecified" and key in their_countries
        )

        sizes = [theirs_size, ours_size, other_size]

        # Calculate the cumulative sum of sizes to position the labels
        cumulative_sizes = [
            sum(sizes[: i + 1]) / sum(sizes) * 100 for i in range(len(sizes))
        ]
        cumulative_sizes.insert(
            0, 0
        )  # Add a zero at the start for the first label position

        # Plotting the bar chart
        fig, ax = plt.subplots(figsize=(14, 1))

        # Create horizontal bars
        bar_widths = [size / sum(sizes) * 100 for size in sizes]
        colors = ["#e41a1c", "#4daf4a", "#FAD02C"]  # Red, Green, Yellow

        bars = ax.barh(
            y=0, width=bar_widths, left=cumulative_sizes[:-1], color=colors, align="center"
        )

        # Add labels inside the bands
        for i, bar in enumerate(bars):
            width = bar.get_width()
            x_position = bar.get_x() + width / 100
            ax.text(
                x_position,
                bar.get_y(),
                f"{sizes[i]}%",
                ha="left",
                va="bottom",
                color="white",
                fontweight="bold",
            )

        ax.set_yticks([])
        ax.set_xlim(0, 100)

        # Adding titles and labels
        ax.set_title(f"Political Breakdown of Contributions for {repo}")
        ax.set_xlabel("Contributions (%)")

        # Show the bar chart
        plt.show()


    def adversarial_pie_chart(self, repo: str):

        values = EnrichmentsClient().threat_summary(repo, adversarial=True).dict()[0]["adversarial_totals"][0]

        # Prepare data for the pie chart
        labels = []
        for value in values.keys():
            labels.append(self.to_title_case(value))
        sizes = list(values.values())

        # Make a "Normal" commits category
        labels.append("Normal")
        sizes.append(100 - sum(sizes))

        # Plotting the pie chart
        plt.figure(figsize=(14, 11))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"Adversarial Commit Distribution in {self.to_title_case(repo)}")
        plt.axis("equal")  # Equal aspect ratio ensures that pie chart is drawn as a circle.

        # Show the pie chart
        plt.show()
