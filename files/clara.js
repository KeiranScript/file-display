const message = "I love you, Clara";
const heart = "❤️";
const printMsg = (msg, emoji) => {
    const format = `
        ${emoji} ${msg} ${emoji}
        ${' '.repeat(10)}  `;
    console.log(format);
};
printMsg(message, heart);
