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