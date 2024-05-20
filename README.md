# DiscordAudioReactor

**DiscordAudioReactor** is a Discord bot designed to listen to conversations in text channels and play specific audio files when certain keywords are detected. This bot adds a fun and interactive element to your Discord server by providing audio reactions based on user-defined keywords.

## Features

- **Keyword Detection**: The bot listens for predefined keywords in text channels.
- **Audio Playback**: Plays corresponding audio files in a voice channel when keywords are detected.
- **Voice Channel Commands**: Commands to make the bot join or leave voice channels.


## Setup

1. Create a new application and bot on the [Discord Developer Portal](https://discord.com/developers/applications).
2. Copy your bot token.
3. Create a `.env` file in the root directory of your project and add your bot token:
    ```
    DISCORD_BOT_TOKEN=your_bot_token_here
    ```

4. Update the `keywords` dictionary in `bot.py` with your desired keywords and corresponding audio file paths.

## Usage

1. Run the bot:
    ```bash
    python bot.py
    ```

2. Use the following commands in your Discord server:
    - `!join`: Make the bot join your current voice channel.
    - `!leave`: Disconnect the bot from the voice channel.

3. The bot will listen for keywords in text channels and play the corresponding audio files in the voice channel.

## Example

```python
keywords = {
    "hello": "path/to/hello.mp3",
    "bye": "path/to/bye.mp3"
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py)
- [PyNaCl](https://github.com/pyca/pynacl)
- [FFmpeg](https://ffmpeg.org/)

```

This `README.md` provides a clear and concise overview of the project, including setup, usage, and contribution guidelines. You can adjust any specific details as needed for your project.
