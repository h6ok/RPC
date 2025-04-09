import RpcClient from './rpcClient';
import question from './question';


const main = async() => {

    try {

        const conn = new RpcClient('localhost', 8080);

        while (true) {
            try {
                const input = await question.rpcQuestion();
                const result = await conn.send(input);
                console.log(`SUCCESS: ${result}`);
            }
            catch (error) {
                console.log(`ERROR: ${error}`);
            }
            finally {
                const input = await question.question('do you wanna try again?');
                if (input.toLowerCase().includes('no') || input.toLowerCase() == 'n') {
                    process.exit(0);
                }
            }
        }
    }
    catch (error) {
        console.log(error);
        return;
    }
}

main();
