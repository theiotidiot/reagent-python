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

# foreign_influence command
@enrichments.command()
@click.option("--entity_name", help="The entity name.")
@click.option("--limit", default=10, help="The number of entities to return.")
@click.option("--entity_type", help="The entity type.")
@click.option("--no_unspecified", help="Whether to exclude unspecified entities.")
@click.option("--start_date", help="The start date of the entity.")
@click.option("--end_date", help="The end date of the entity.")
def foreign_influence(entity_name, limit, entity_type, no_unspecified, start_date, end_date):
    """Given a repo name, get a snapshot of foreign influence on all commits in the repo."""
    client = Reagent().enrichments()
    response = client.foreign_influence(
        entity_name=entity_name, limit=limit, entity_type=entity_type, no_unspecified=no_unspecified, start_date=start_date, end_date=end_date
    )
    click.echo(response.text())

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
@click.option("--repo", help="The repo name.")
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
