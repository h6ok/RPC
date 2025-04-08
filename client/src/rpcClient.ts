import Request from "./request";

class RpcClient {

    address: string;
    port: number;
    request: Request;

    constructor(address: string, port: number) {
        this.address = address;
        this.port = port;
    }

    send (input: string): Promise<string> {
        const method = input[0];
        const params = input.split(' ').slice(1, input.split('').length);
            
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
                return 'function [' + method + '] is not supplied';
        }
    }

    floor (params: string[]): string{
        const request = new Request('floor', params);
        const jsonReq = request.toJson();

        return '';
    }

    nroot (params: string[]): string{

        return new Promise((resolve, reject) => {
            
        })
        const request = new Request('nroot', params);
        const jsonReq = request.toJson();

        return '';
    }

    validAnagram (params: string[]): string{
        const request = new Request('validAnagram', params);
        const jsonReq = request.toJson();

        return '';
    }

    reverse (params: string[]): string{
        const request = new Request('reverse', params);
        const jsonReq = request.toJson();

        return '';
    }

    sort (params: string[]): string{
        const request = new Request('sort', params);
        const jsonReq = request.toJson();

        return '';
    }
}

export default RpcClient;