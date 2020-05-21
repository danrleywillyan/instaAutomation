# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'gamacidadao'
insta_password = 'abcdE123321'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

with smart_run(session):
    """ Activity Follow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    min_followers=100,
                                    min_following=40)

    session.set_dont_include(["taurus.py", 'rodrigowebcarvalho'])
    session.set_dont_like(["pizza", "#store"])

    # activities

    """ First step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)...
    """
    # session.follow_user_followers(['avogamaavogama'], amount=3000, randomize=False, interact=False)
