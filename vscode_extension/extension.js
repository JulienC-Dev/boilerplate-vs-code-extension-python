const vscode = require('vscode');
const { exec } = require('child_process');
const path = require('path');

function activate(context) {
    console.log('Congratulations, your extension Update Account is now active!');

    let disposable = vscode.commands.registerCommand('app.updateAccount', (uri) => {
        const dirPath = path.dirname(uri.fsPath);
        const command = `source ${dirPath}/venv/bin/activate && python3.8 ${dirPath}/myapp/main.py -p ${uri.fsPath}`;
        exec(command, { shell: '/bin/bash' }, (error, stdout, stderr) => {
            if (error) {
                vscode.window.showErrorMessage(`Error: ${error.message}`);
                return;
            }
            if (stderr) {
                vscode.window.showWarningMessage(`Stderr: ${stderr}`);
                return;
            }
            vscode.window.showInformationMessage(`Output: ${stdout}`);
        });
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
