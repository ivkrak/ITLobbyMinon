
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from src.config import logger

from src.config import BOT_ADMIN_ID
from src.utils.keyboards.admin import admin_panel_kb

router = Router()


@router.message(Command('admin'))
@router.message(F.text == 'Вернуться в меню')
async def admin_panel(message: Message, state: FSMContext):
    logger.debug(f'ID пользователя: {message.from_user.id}')
    if message.from_user.id == BOT_ADMIN_ID:
        await message.answer(
            'Добро пожаловать в меню администратора!',
            reply_markup=admin_panel_kb
        )
        logger.debug(f'Пользователь {message.from_user.full_name} вошел в админ панель')
    await state.clear()
    await message.delete()
