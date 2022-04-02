import DiscordJS, { Intents, Message } from 'discord.js'
import dotenv from 'dotenv'


dotenv.config()

const client = new DiscordJS.Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES
    ]
})

client.on('ready', () => {
    console.log('The bot is ready')
})

client.on('messageCreate', (message) => {
    if(message.content === '$concerndle'){
        //will create this function later
        message.reply({
            content: 'wassup',
        })
        //message.startGame();
    }
})


client.login(process.env.TOKEN)