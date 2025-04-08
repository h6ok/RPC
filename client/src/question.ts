import readline from 'node:readline';

const question = async(): Promise<string> => {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    return new Promise((resolve, reject) => {

        rl.question(
            'what function you wanna call ?\n'
            + '・floor(x: double)  return int value\n'
            + '・nroot(x: int, y: int) return value which is value ** x = y\n'
            + '・reverse(s: string) return reversed string\n'
            + '・validAnagram(s1: string, s2: string) return whether two parameter string is anagram\n'
            + '・sort(strArr: []string) return sorted string array\n\n'
            , callable => {
                if (callable == 'exit') {
                    reject(callable);
                    rl.close();
                    return;
                }
                resolve(callable);
                rl.close();
            }
        );
    })
}

export default question;