fun = async (url) => {  // Creates an async object function. Allowing the use of await. 
    let response = await fetch(url) // await only used inside async function. Pauses function execution, awaiting promise. Fetch collected the data as a Promise from the URL.
    let obj = await response.json()  // Converts to JSON format.
    let data = obj.message  // "message" is the value contained within Json.
    return data
}

let api_Url = ""  // API URL.
fun(api_Url).then(
    function(value){
        console.log("Then: ", value)  // Execute if successful
    },
    function(error){
        console.error("Then: ", error)  // Execute if unsuccessful
    }
)

try{
    fun(hello)
    console.log("Try: ", "Done")  // Execute if successful
}
catch(error){
    console.error("Catch: ", error)  // Execute if unsuccessful
}
