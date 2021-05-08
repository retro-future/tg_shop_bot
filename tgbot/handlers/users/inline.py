from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.loader import dp
from tgbot.filters import IsSubcategoryName
from tgbot.utils.db_api.quick_commands import show_products_inline


@dp.inline_handler(IsSubcategoryName(), regexp="^.{4,}")
async def inline_products(query: types.InlineQuery, state: FSMContext):
    query_text = query.query
    query_answer, first_product = await show_products_inline(query_text, state)
    await state.update_data(product_data={
        "subcategory_name": first_product.parent.tg_name,
        "category_id": first_product.parent.category_id,
        "subcategory_id": first_product.parent.id
    })
    await query.answer(results=query_answer, cache_time=0)
