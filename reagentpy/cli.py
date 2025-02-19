from typing import Optional
import click
from reagentpy import Reagent

# CLI entry point
@click.group()
def cli():
    """Python wrapper for the Reagent Analytics API."""
    pass

# login command
@cli.group()
@click.option("--username", prompt=True, help="Your Reagent username")
@click.option("--password", prompt=True, hide_input=True, help="Your Reagent password")
def login(username, password):
    """Login to the Reagent API."""
    pass

# status command
@cli.command()
def status():
    """Get status of the Reagent API."""
    response = Reagent().status()
    click.echo(response.text())

# community client
@cli.group()
def community():
    """Community related commands."""
    pass

# maintainers command
@community.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of maintainers to return.")
@click.option("--email", help="The email of the maintainer.")
@click.option("--name", help="The name of the maintainer.")
def maintainers(repo, limit, email, name):
    """Get maintainers of a repo."""
    client = Reagent().community()
    response = client.maintainers(repo=repo, limit=limit, email=email, name=name)
    click.echo(response.text())

# communities command
@community.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of communities to return.")
@click.option("--timezone", help="The timezone of the communities.")
@click.option("--start_date", help="The start date of the communities.")
@click.option("--end_date", help="The end date of the communities.")
def communities(repo, limit, timezone, start_date, end_date):
    """Get communities of a repo."""
    client = Reagent().community()
    response = client.communities(repo=repo, limit=limit, timezone=timezone, start_date=start_date, end_date=end_date)
    click.echo(response.text())

# enrichments client
@cli.group()
def enrichments():
    """Enrichments related commands."""
    pass

# hibp command
@enrichments.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of breaches to return.")
@click.option("--breach", help="The breach name.")
@click.option("--email", help="The email address.")
@click.option("--timezone", help="The timezone.")
def hibp(repo, limit, breach, email, timezone):
    """Given a repo name or email address, get all data breaches the entity is a part of."""
    client = Reagent().enrichments()
    response = client.hibp(repo=repo, limit=limit, breach=breach, email=email, timezone=timezone)
    click.echo(response.text())

# similar_repos command
@enrichments.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of similar repos to return.")
@click.option("--email", help="The email address.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
def similar_repos(repo, limit, email, timezone, start_date, end_date):
    """Given a repository, get similar organizations and tags common between them."""
    client = Reagent().enrichments()
    response = client.similar_repos(repo=repo, limit=limit, email=email, timezone=timezone, start_date=start_date, end_date=end_date)
    click.echo(response.text())

# timezone_spoof command
@enrichments.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of timezones to return.")
def timezone_spoof(repo, limit):
    """Given a repo name, get all fabricated timezone information."""
    client = Reagent().enrichments()
    response = client.timezone_spoof(repo=repo, limit=limit)
    click.echo(response.text())

# topics command
@enrichments.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of topics to return.")
@click.option("--email", help="The email address.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
def topics(repo, limit, email, timezone, start_date, end_date):
    """Given a repo name, get all topics."""
    client = Reagent().enrichments()
    response = client.topics(repo=repo, limit=limit, email=email, timezone=timezone, start_date=start_date, end_date=end_date)
    click.echo(response.text())

# repo client
@cli.group()
def repo():
    """Repo related commands."""
    pass

# email_domains command
@repo.command()
@click.option("--repo-name", help="The repo name.")
@click.option("--limit", default=10, help="The number of email domains to return.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
def email_domains(repo, limit, timezone, start_date, end_date):
    """Given a repository, get all the other organizations that contributing users are working in."""
    client = Reagent().repo()
    response = client.email_domains(repo=repo, limit=limit, timezone=timezone, start_date=start_date, end_date=end_date)
    click.echo(response.text())

# timezones command
@repo.command()
@click.option("--repo", help="The repo name.")
@click.option("--email", help="The email address.")
@click.option("--timezone", help="The timezone.")
@click.option("--name", help="The name.")
def timezones(repo, email, timezone, name):
    """Given a repo name, get number of commits and timezone data."""
    client = Reagent().repo()
    response = client.timezones(repo=repo, email=email, timezone=timezone, name=name)
    click.echo(response.text())

# hygiene_summary command
@repo.command()
@click.option("--repo", help="The repo name.")
def hygiene_summary(repo):
    """Given a repo name, get a high-level summary of its general open-source best practices."""
    client = Reagent().repo()
    response = client.hygiene_summary(repo=repo)
    click.echo(response.text())

# repo_list command
@repo.command()
@click.option("--limit", default=10, help="The number of users to return.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
def repo_list(limit, timezone, start_date, end_date):
    """Given a repo name, get a high-level summary of its general open-source best practices."""
    client = Reagent().repo()
    response = client.repo_list(limit=limit, timezone=timezone, start_date=start_date, end_date=end_date)
    click.echo(response.text())

# user_commit_data command
@repo.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of users to return.")
@click.option("--email", help="The email address.")
@click.option("--name", help="The name.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
@click.option("--order_by_date", help="Whether to order by date.")
@click.option("--include_other_repos", help="Whether to include other repos.")
@click.option("--format_in_rows", help="Whether to format in rows.")
def user_commit_data(repo, limit, email, name, timezone, start_date, end_date, order_by_date, include_other_repos, format_in_rows):
    """Given a repo name and timezone, get users above a certain threshold for finer-grained intelligence."""
    client = Reagent().repo()
    response = client.user_commit_data(
        repo=repo, limit=limit, email=email, name=name, timezone=timezone, start_date=start_date, end_date=end_date, order_by_date=order_by_date, include_other_repos=include_other_repos, format_in_rows=format_in_rows
    )
    click.echo(response.text())

# user client
@cli.group()
def user():
    """User related commands."""
    pass

# commit_file_community command
@user.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of commits to return.")
@click.option("--email", help="The email address.")
@click.option("--name", help="The name.")
@click.option("--order_by_date", help="Whether to order by date.")
@click.option("--format_in_rows", help="Whether to format in rows.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
def commit_file_community(repo, limit, email, name, order_by_date, format_in_rows, timezone, start_date, end_date):
    """Get threat scores, repos, and top developers on files."""
    client = Reagent().user()
    response = client.commit_file_community(
        repo=repo, limit=limit, email=email, name=name, order_by_date=order_by_date, format_in_rows=format_in_rows, timezone=timezone, start_date=start_date, end_date=end_date
    )
    click.echo(response.text())

# post_patch command
@user.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of commits to return.")
@click.option("--email", help="The email address.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
def post_patch(repo, limit, email, timezone, start_date, end_date):
    """Get everything a user has done, sorting by most recent suspicious activity and whether their potentially introduced security vulnerabilities have been patched."""
    client = Reagent().user()
    response = client.post_patch(repo=repo, limit=limit, email=email, timezone=timezone, start_date=start_date, end_date=end_date)
    click.echo(response.text())

# profile command
@user.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of commits to return.")
@click.option("--email", help="The email address.")
@click.option("--name", help="The name.")
@click.option("--timezone", help="The timezone.")
@click.option("--start_date", help="The start date.")
@click.option("--end_date", help="The end date.")
def profile(repo, limit, email, name, timezone, start_date, end_date):
    """Get contributor profiles for a given user."""
    client = Reagent().user()
    response = client.profile(repo=repo, limit=limit, email=email, name=name, timezone=timezone, start_date=start_date, end_date=end_date)
    click.echo(response.text())

# timezone visualization client
@cli.group()
def timezone_visualizations():
    """Timezone visualization commands."""
    pass

# show_logarithmic_bar_chart visualization command
@timezone_visualizations.command()
@click.option("--api-response", help="API query response from RepoClient().timezones")
def show_logarithmic_bar_chart(api_response):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().timezone_visualizations()
    response = client.show_logarithmic_bar_chart(response=api_response)
    click.echo(response.text())

# plot_timezone_distribution visualization command
@timezone_visualizations.command()
@click.option("--api-response", help="API query response from RepoClient().timezones")
def plot_timezone_distribution(api_response):
    """Visualize timezones in a bar chart!"""
    client = Reagent().timezone_visualizations()
    response = client.plot_timezone_distribution(response=api_response)
    click.echo(response.text())

# plot_timezone_distribution_color visualization command
@timezone_visualizations.command()
@click.option("--api-response", help="API query response from RepoClient().timezones")
def plot_timezone_distribution_color(api_response):
    """Visualize timezones in a (colored) bar chart!"""
    client = Reagent().timezone_visualizations()
    response = client.plot_timezone_distribution_color(response=api_response)
    click.echo(response.text())

# get_top_n_timezones visualization command
@timezone_visualizations.command()
@click.option("--api-response", help="API query response from RepoClient().timezones")
@click.option("--timezone-count", default=10, help="Top number of timezones to return, in order")
def get_top_n_timezones(api_response, tz_count):
    """List each timezone commits occur in within a given repo, from most to least!"""
    client = Reagent().timezone_visualizations()
    response = client.get_top_n_timezones(response=api_response, N=tz_count)
    click.echo(response.text())

# build_and_show_timezone_map visualization command
@timezone_visualizations.command()
@click.option("--api-response", help="API query response from RepoClient().timezones")
def build_and_show_timezone_map(api_response):
    """List each timezone commits occur in within a given repo, from most to least!"""
    client = Reagent().timezone_visualizations()
    response = client.build_and_show_timezone_map(response=api_response)
    click.echo(response.text())

# demo (all other) visualization client
@cli.group()
def demo_visualizations():
    """Generic visualization commands, originally used in demos."""
    pass

# wordcloud visualization command
@demo_visualizations.command()
@click.option("--api-response", help="API query response from RepoClient().email_donains")
def wordcloud(api_response):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().demo_visualizations()
    response = client.wordcloud(response=api_response)
    click.echo(response.text())

# print_hygiene_summary visualization command
@demo_visualizations.command()
@click.option("--api-response", help="API query response from RepoClient().email_donains")
def print_hygiene_summary(api_response):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().demo_visualizations()
    response = client.print_hygiene_summary(response=api_response)
    click.echo(response.text())

# create_out_of_five_chart visualization command
@demo_visualizations.command()
@click.option("--repo", help="The repo name.")
@click.option("--limit", default=10, help="The number of commits to return.")
def create_out_of_five_chart(repo: Optional[str], limit: Optional[int]):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().demo_visualizations()
    response = client.create_out_of_five_chart(repo=repo, limit=limit)
    click.echo(response.text())

# nationality_pie_chart visualization command
@demo_visualizations.command()
@click.option("--repo", help="The repo name.")
@click.option("--country-counts", default=10, help="The number of commits per country.")
def nationality_pie_chart(country_counts, repo):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().demo_visualizations()
    response = client.nationality_pie_chart(country_counts, repo)
    click.echo(response.text())

# nationality_horizontal_bar_chart visualization command
@demo_visualizations.command()
@click.option("--repo", help="The repo name.")
@click.option("--country-counts", default=10, help="The number of commits per country.")
def nationality_horizontal_bar_chart(country_counts, repo):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().demo_visualizations()
    response = client.nationality_horizontal_bar_chart(country_counts, repo)
    click.echo(response.text())

# hibp_pie_chart visualization command
@demo_visualizations.command()
@click.option("--repo", help="The repo name.")
def hibp_pie_chart(repo):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().demo_visualizations()
    response = client.hibp_pie_chart(repo)
    click.echo(response.text())

# political_chart visualization command
@demo_visualizations.command()
@click.option("--repo", help="The repo name.")
@click.option("--country-counts", default=10, help="The number of commits per country.")
def political_chart(country_counts, repo):
    """Visualize timezones in a bar chart, scaled logarithmically for readability!"""
    client = Reagent().demo_visualizations()
    response = client.political_chart(country_counts, repo)
    click.echo(response.text())
