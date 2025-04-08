import RpcClient from './rpcClient';
import question from './question';


const main = async() => {

    try {

        const conn = new RpcClient('localhost', 8080);

        while (true) {
            try {
                const input = await question();
                const result = await conn.send(input);
                console.log(`rpc result is ${result}`);
            }
            catch {
                console.log('see you soon!');
                break;
            }
        }
    }
    catch (error) {
        console.log(error);
        return;
    }
}

main();
