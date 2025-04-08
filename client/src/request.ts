class Request {

    method: string;
    params: string[];
    params_type: string[];

    constructor(method: string, params: string[]) {
        this.method = method;
        this.params = params;
        this.params_type = params.map(c => typeof c)
    }

    toJson(): string {
        return JSON.stringify(this);
    }
}

export default Request;