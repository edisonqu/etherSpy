function takeValue(event) {
    event.preventDefault()
    window.location.href="/thankyou";


    var blockchainAddress = document.getElementById("blockchain").value
    var phoneNumber = document.getElementById("phones").value

    console.log(blockchainAddress)
    console.log(phoneNumber)

    fetch('http://127.0.0.1:5000/sendMessage',{method: 'POST',
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
            console.log(data);
            })
})
}

