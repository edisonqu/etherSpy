function takeValue(event) {
    event.preventDefault()


    var blockchainAddress = document.getElementById("blockchain").value
    var phoneNumber = document.getElementById("phones").value

    console.log(blockchainAddress)
    console.log(phoneNumber)

    fetch('/sendMessage',{method: 'POST',
        headers: {
        'Content-Type': 'application/json',
      },
        body: JSON.stringify({
            "blockchain": blockchainAddress,
            "phone_number": phoneNumber
        }),
     })
        .then((data )=>{
            data.text().then((data) => {
                dataInfo = data
                if(data === "finished"){
                        window.location.href="/thankyou";
                }
            console.log(data);
            })
})
}

