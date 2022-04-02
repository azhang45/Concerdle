import DiscordJS, { Intents, Message } from 'discord.js'
import dotenv from 'dotenv'


dotenv.config()

const client = new DiscordJS.Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES3
    ]
})

client.on('ready', () => {
    console.log(`${client.user.tag} has logged in`);
})

client.on('messageCreate', (message) => {
    if(message.content === '$concerndle'){
        //will create this function later
        message.reply({
            content: 'wassup',
        })
        //message.startGame();
        //once start game is called will do message.content.substring(0, 7) === '$guess'
    }
})


client.login(process.env.TOKEN)