console.log("Connected to client.js")

function deleteRowTemplate(url, tableName, rowId) {
    $.ajax(url, {
        contentType: "application/json",
        data: JSON.stringify({
            'rowId': rowId,
            'tableName': tableName,
            'request': 'delete'
        }),
        type: 'POST',
        success: function (data) {
            let newDoc = document.open("text/html", "replace");
            newDoc.write(data);
            newDoc.close();
        }
    });
}

function addRowTemplate(url, tableName, data) {
    $.ajax(url, {
        contentType: "application/json",
        data: JSON.stringify({
            'tableName': tableName,
            'request': 'add',
            'data': data
        }),
        type: 'POST',
        success: function (data) {
            let newDoc = document.open("text/html", "replace");
            newDoc.write(data);
            newDoc.close();
        }
    });
}

function updateRowTemplate(url, tableName, data) {
    $.ajax(url, {
        contentType: "application/json",
        data: JSON.stringify({
            'tableName': tableName,
            'request': 'update',
            'data': data
        }),
        type: 'POST',
        success: function (data) {
            let newDoc = document.open("text/html", "replace");
            newDoc.write(data);
            newDoc.close();
        }
    });
}