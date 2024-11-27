from aiogram import Bot
from aiogram.types import BufferedInputFile


class SendFile:
    def __init__(self, token: str):
        self.bot = Bot(token=token)

    async def send_file_audio(
        self,
        chat_id: int,
        file,
        filename: str,
        caption: str = "Загружен новый урок (аудио)",
    ):
        """
        Отправляет аудиофайл в Telegram.

        :param chat_id: ID чата, куда отправляется файл.
        :param file: Файл в виде байтов.
        :param filename: Имя файла.
        :param caption: Подпись к файлу.
        """ 
        try:
            tg_file = BufferedInputFile(file, filename)  # Создаем буферизированный файл
            result = await self.bot.send_audio(
                chat_id=chat_id, audio=tg_file, caption=caption
            )
            print("Файл успешно отправлен.")
            return result.audio.file_id  # Возвращаем file_id
        except Exception as e:
            print(f"Ошибка при отправке файла: {e}")

    async def shutdown_bot(self):
        await self.bot.session.close()
