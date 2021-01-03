import royalnet.engineer as engi


@engi.PartialCommand.new(name="ping", syntax="")
def ping(_sentry: engi.Sentry, _msg: engi.Message, **__):
    """
    A way to check if the bot is working: it will always reply to this command with "🏓 Pong!".
    """
    await _msg.send_reply("🏓 Pong!")


__all__ = ("ping",)