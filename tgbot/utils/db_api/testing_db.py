import asyncio
import gino
from tgbot.utils.db_api.db_gino import db
from tgbot.data import config
from tgbot.utils.db_api.quick_commands import get_user
from tgbot.utils.db_api.schemas.goods import TgUserGino, OrdersGino, ProductGino


async def test():
    engine = await gino.create_engine(config.POSTGRES_URI)
    db.bind = engine
    # result = await get_parent_child()
    # for i in result:
    #     print(i.children)
    # user = await TgUserGino.get(4)
    # await user.update(name="Ilona").apply()
    product = await ProductGino.query.where(ProductGino.title.ilike("%xiaomi%")).gino.all()
    user = await get_user(92613407)
    for i in product:
        print(i.title)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
