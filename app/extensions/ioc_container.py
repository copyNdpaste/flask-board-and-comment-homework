import inject

from core.repository.repository import Repository


def init_provider():
    inject.clear_and_configure(
        lambda binder: binder.bind_to_provider(Repository, Repository)
    )
