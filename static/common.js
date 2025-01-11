function common_ajax(formdata, url_str, request_method, call_back_function){
    $.ajax({
        url:url_str,
        method:request_method,
        data:formdata,
        success:function(response){
            call_back_function(response)
        }
    })
}