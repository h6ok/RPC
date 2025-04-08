import net from 'node:net';
import Request from "./request";

class RpcClient {

    address: string;
    port: number;
    socket: net.Socket;


    constructor(address: string, port: number) {
        this.address = address;
        this.port = port;
        this.socket = net.connect(port, address);
    }

    send (input: string): Promise<string> {

        const [method, ...params] = input.split(' ');
            
        switch (method) {
            case 'floor':
                return this.floor(params);

            case 'nroot':
                return this.nroot(params);

            case 'validAnagram':
                return this.validAnagram(params);

            case 'reverse':
                return this.reverse(params);

            case 'sort':
                return this.sort(params);

            default:
                return new Promise(resolve => resolve('function [' + method + '] is not supplied'));
        }
    }

    floor (params: string[]): Promise<string> {
        const request = new Request('floor', params);
        const jsonReq = request.toJson();
        return this.write(jsonReq);
    }

    nroot (params: string[]): Promise<string>{
        const request = new Request('nroot', params);
        const jsonReq = request.toJson();
        return this.write(jsonReq);
    }

    validAnagram (params: string[]): Promise<string>{
        const request = new Request('validAnagram', params);
        const jsonReq = request.toJson();
        return this.write(jsonReq);
    }

    reverse (params: string[]): Promise<string>{
        const request = new Request('reverse', params);
        const jsonReq = request.toJson();
        return this.write(jsonReq);
    }

    sort (params: string[]): Promise<string>{
        const request = new Request('sort', params);
        const jsonReq = request.toJson();
        return this.write(jsonReq);
    }

    write (jsonStr: string): Promise<string> {
        return new Promise((resolve, reject) => {

            this.socket.once('data', (data: string) => {

                const res = JSON.parse(data);
                if (res.error) {
                    reject();
                    return;
                }

                resolve(res.result);
            })

            this.socket.write(jsonStr);
        }); 
    }
}

export default RpcClient;