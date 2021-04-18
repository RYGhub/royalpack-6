import royalnet.engineer as engi
import royalnet.engineer.conversation as c
import royalnet_telethon
import royalnet_telethon.bullet.contents


@engi.TeleportingConversation
async def ciaoruozi(*, _sentry: engi.Sentry, _msg: engi.Message, _imp, **__):
    """
    Saluta Ruozi, una creatura leggendaria che potrebbe esistere o non esistere in Royal Games.
    """

    if isinstance(_imp, royalnet_telethon.TelethonPDAImplementation):
        sender: royalnet_telethon.bullet.contents.TelegramUser = await _msg.sender
        # noinspection PyProtectedMember
        if sender._user.id == 112437036:
            await _msg.reply(text="👋 Ciao me!")

    await _msg.reply(text="👋 Ciao Ruozi!")


__all__ = ("ciaoruozi",)