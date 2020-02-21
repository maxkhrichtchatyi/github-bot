import asyncio
import os

from aiohttp.client import ClientSession
from octomachinery.github.api.tokens import GitHubOAuthToken
from octomachinery.github.api.raw_client import RawGitHubAPI


async def main():
    access_token = GitHubOAuthToken(os.environ['GITHUB_TOKEN'])
    async with ClientSession() as http_session:
        gh = RawGitHubAPI(
            access_token,
            session=http_session,
            user_agent='j0shu4b0y',
        )

        # await gh.post(
        #     '/repos/mariatta/strange-relationship/issues',
        #     data={
        #         'title': 'We got a problem',
        #         'body': 'Use more emoji!',
        #     },
        # )

        await gh.post(
            '/repos/mariatta/strange-relationship/issues/256',
            data={
                'state': 'closed',
            },
        )


asyncio.run(main())

#  27584b8e361872446650476ae3c2b2c94952b9aa
