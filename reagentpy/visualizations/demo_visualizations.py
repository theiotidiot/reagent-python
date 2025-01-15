import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from reagentpy.clients.enrichments import EnrichmentsClient
from reagentpy.ReagentClient import ReagentClient


class DemoVisClient(ReagentClient):
    def __init__(self):
        super().__init__()

    def to_title_case(self, start_string: str) -> str:
        return start_string.replace("_", " ").title()


    def wordcloud(self, response):
        word_freq_dict = {item.domain: item.instances for item in response}
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


    def print_hygiene_summary(self, response):
        print(
            "\033[1mRepository Overview:\033[0m \033[94m"
            + response.repo_name
            + "\033[0m\n"
            "\033[1mDescription:\033[0m " + response.description + "\n"
            "\033[1mTotal Contributors:\033[0m "
            + str(response.total_contributors)
            + ", spanning across "
            + str(response.total_timezones)
            + " timezones, indicating a global contribution pattern.\n"
            "\033[1mFork Count:\033[0m "
            + str(response.forks)
            + ", showcasing the community engagement and interest.\n"
            "\033[1mLicense Presence:\033[0m "
            + ("Yes" if response.has_license else "No")
            + ", an important aspect of open source software.\n"
            "\033[1mReadme Presence:\033[0m "
            + ("Yes" if response.has_readme else "No")
            + ", vital for repository documentation.\n"
            "\033[1mRecent Commit:\033[0m "
            + ("Available" if response.last_activity_at else "Not Available")
            + ", indicating the current activity status."
        )


    def create_out_of_five_chart(self, repo: str | None = None, limit: int | None = 50):

        data = EnrichmentsClient.threat_scores_for_visualizations(repo, limit)

        values = data[0]

        # Create and display charts for each metric
        for raw_title, score in values:

            if score is None:
                score = 0
            else:
                score = score / 2

            title = f"{raw_title.replace('_', ' ').title()}"

            fig, ax = plt.subplots(figsize=(10, 2))

            ax.barh(y=0, width=10, color="skyblue", align="center")
            # Create the foreground bar (actual score)
            ax.barh(y=0, width=score, color="orange", align="center")

            ax.set_xlim(0, 5)
            ax.set_yticks([])
            ax.set_xlabel("Threat Score out of 5")
            ax.set_title(title)

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


    def hibp_pie_chart(self, repo: str):
        try:
            hibp_counts = EnrichmentsClient.hibp_for_visualizations(repo)

        except Exception as e:
            print("An error occurred: ", e, file=sys.stderr)
            raise e

        # Prepare data for the pie chart
        labels = list(hibp_counts.keys())
        sizes = list(hibp_counts.values())

        # Plotting the pie chart
        plt.figure(figsize=(14, 11))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"Data Breaches in: {repo}")
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


    def threat_summary_horizontal_bar_chart(self, summaries, summary_type: str, repo):

        print("DATA: " + str(summaries))

        if summary_type.lower() == "nonadversarial":
            data_dict = summaries.nonadversarial_totals

        elif summary_type.lower() == "adversarial":
            data_dict = summaries.adversarial_totals

        else:
            raise ValueError(
                "Unsupported summary type. Use 'nonadversarial' or 'adversarial'."
            )

        # Aggregate the scores
        aggregate_scores = {}
        for key, _ in data_dict.items():
            aggregate_scores[self.to_title_case(key)] = data_dict[key]

        # Prepare data for the bar chart
        labels = list(aggregate_scores.keys())
        sizes = [aggregate_scores[label] for label in labels]

        # Calculate the cumulative sum of sizes to position the labels
        total_size = sum(sizes)
        sizes = [size / total_size * 100 for size in sizes]
        cumulative_sizes = [sum(sizes[: i + 1]) for i in range(len(sizes))]
        cumulative_sizes.insert(
            0, 0
        )  # Add a zero at the start for the first label position

        # Plotting the bar chart
        fig, ax = plt.subplots(figsize=(14, 2))

        # Create horizontal bars
        colors = plt.get_cmap("tab20")(range(len(sizes)))  # Generate distinct colors

        bars = ax.barh(
            y=0, width=sizes, left=cumulative_sizes[:-1], color=colors, align="center"
        )

        # Add a legend
        legend_patches = [plt.Rectangle((0, 0), 1, 1, fc=color) for color in colors]
        ax.legend(
            legend_patches,
            aggregate_scores,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.15),
            ncol=4,
        )

        # Adjust layout to make room for legend
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.3)

        if summary_type.lower() == "nonadversarial":
            # Add labels inside the bands
            for i, bar in enumerate(bars):
                width = bar.get_width()
                x_position = bar.get_x() + width / 2
                ax.text(
                    x_position,
                    bar.get_y(),
                    labels[i] + ": {0:.2f}".format(aggregate_scores[labels[i]]),
                    ha="center",
                    va="bottom",
                    color="white",
                    fontweight="bold",
                )
            ax.set_yticks([])
            ax.set_xlim(0, 100)

            # Adding titles and labels
            ax.set_title(f"Non-Adversarial Threat Metrics for {repo}")
        else:
            for i, bar in enumerate(bars):
                width = bar.get_width()
                x_position = bar.get_x() + width / 2
                ax.text(
                    x_position,
                    bar.get_y(),
                    "{0:.2f}%".format(aggregate_scores[labels[i]]),
                    ha="center",
                    va="bottom",
                    color="white",
                    fontweight="bold",
                )
            ax.set_yticks([])
            ax.set_xlim(0, 100)

            # Adding titles and labels
            ax.set_title(f"Adversarial Commit Percentage for {repo} by Threat Type")

        # Show the bar chart
        plt.show()
