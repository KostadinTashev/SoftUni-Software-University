import os
import django
from django.db.models import Count, Avg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
    if search_name is not None and search_email is not None:
        searched_authors = Author.objects.filter(
            full_name__icontains=search_name,
            email__icontains=search_email
        ).order_by('-full_name')
    elif search_name is not None:
        searched_authors = Author.objects.filter(
            full_name__icontains=search_name
        ).order_by('-full_name')
    elif search_email is not None:
        searched_authors = Author.objects.filter(
            email__icontains=search_email
        ).order_by('-full_name')
    else:
        return ""

    if not searched_authors:
        return ""

    result = []

    for author in searched_authors:
        if author.is_banned:
            status = 'Banned'
        else:
            status = 'Not Banned'
        result.append(f"Author: {author.full_name}, email: {author.email}, status: {status}")

    return '\n'.join(result)


def get_top_publisher() -> str:
    authors = Author.objects.annotate(
        num_articles=Count('articles_authors')
    ).order_by(
        '-num_articles', 'email'
    )

    if not authors:
        return ""

    top_author = authors.first()

    if top_author.num_articles == 0:
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.num_articles} published articles."


def get_top_reviewer() -> str:
    reviewers = Author.objects.annotate(
        num_reviews=Count('reviews_author')
    ).order_by('-num_reviews', 'email')

    if not reviewers:
        return ''
    top_reviewer = reviewers.first()
    if top_reviewer.num_reviews == 0:
        return ''

    return f'Top Reviewer: {top_reviewer.full_name} with {top_reviewer.num_reviews} published reviews.'


def get_latest_article() -> str:
    latest_article = Article.objects.order_by('-published_on').first()

    if not latest_article:
        return ''

    authors = latest_article.authors.all().order_by('full_name')
    author_names = ', '.join([author.full_name for author in authors])
    num_reviews = Review.objects.filter(article=latest_article).count()
    avg_rating = Review.objects.filter(article=latest_article).aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0.0
    return f"The latest article is: {latest_article.title}. Authors: {author_names}. Reviewed: {num_reviews} times. " \
           f"Average Rating: {avg_rating:.2f}."


def get_top_rated_article() -> str:
    top_rated_articles = Article.objects \
        .annotate(
        avg_rating=Avg('articles__rating'),
        num_reviews=Count('articles')) \
        .order_by('-avg_rating', 'title') \
        .filter(num_reviews__gt=0)

    if not top_rated_articles:
        return ""

    top_rated_article = top_rated_articles.first()

    return f"The top-rated article is: {top_rated_article.title}, with an average rating of {top_rated_article.avg_rating:.2f}, reviewed {top_rated_article.num_reviews} times."


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = Author.objects.filter(email=email).first()

    if not author:
        return "No authors banned."

    num_reviews = Review.objects.filter(author=author).count()
    author.is_banned = True
    author.save()

    Review.objects.filter(author=author).delete()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."
