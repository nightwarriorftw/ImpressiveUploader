   $(document).ready(function () {
 
    $('form').on('submit', function (event) {
 
        event.preventDefault();
        
        let pausebtn = document.getElementById("pausebtn");
        let continuebtn = document.getElementById("continuebtn");
        let stopbtn = document.getElementById("stopbtn");
        pausebtn.style.display = "block";

        let bytesLoaded = 0;
        let totalSize = 0;
        let xhr = new window.XMLHttpRequest();
        let formData = new FormData($('form')[0]);
        $.ajax({
            xhr: function () {
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable ) {
                        computableLenth = true;
                        bytesLoaded = e.loaded;
                        totalSize = e.total;
                        console.log('Bytes Loaded: ' + e.loaded);
                        console.log('Total Size: ' + e.total);
                        console.log('Percentage Uploaded: ' + (e.loaded / e.total) * 100)
 
                        let percent = Math.round((e.loaded / e.total) * 100);
                        if(percent == 100) {
                            pausebtn.style.display = continuebtn.style.display = stopbtn.style.display = "none";
                        }
 
                        $('#progressBar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
 
                    }
 
                });
 
                return xhr;
            },
            type: 'POST',
            url: '/api/upload/',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                console.log(response);
                document.getElementById("response").innerHTML = `{"details":${response.details}, "status": ${response.status}}`;
                    
            }
        });

        pausebtn.addEventListener("click", function() {
            console.log("pausing")
            xhr.abort();
            if(pausebtn.style.display == "block") {

                continuebtn.style.display = "block";
                stopbtn.style.display = "block";
            }
        });

        stopbtn.addEventListener("click", function(){
            console.log("Aborted");
            continuebtn.style.display = "none";
            stopbtn.style.display = "none";
            pausebtn.style.display = "none";
            document.getElementById("response").innerHTML = `{"details":"Process Terminated", "status": "200_OK"}`
            xhr.abort();
        });

        continuebtn.addEventListener("click", function(event){
            //stating again
            document.getElementById("action").innerHTML = "{'details':'Process started again'}";
            $.ajax({
                xhr: function () {
                    xhr.upload.addEventListener('progress', function(e) {
                        if (e.computableLenth) {
                            console.log('Bytes Loaded: ' + bytesLoaded);
                            console.log('Total Size: ' + totalSize);
                            console.log('Percentage Uploaded: ' + (totalSize / bytesLoaded) * 100)
    
                            let percent = Math.round((totalSize / bytesLoaded) * 100);
                            //let percent2 = Math.round((totalSize/bytesLoaded) * 100);
                            if(percent == 100) {
                                pausebtn.style.display = continuebtn.style.display = stopbtn.style.display = "none";
                            }
                            // if(percent < percent2) {
                            //    continue;
                            // }
                            //else{
                            document.getElementById("response").innerHTML = percent;
                            //}
                        }
    
                    });
    
                    return xhr;
                },
                type: 'POST',
                url: '/api/upload/',
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    console.log(response);
                    document.getElementById("response").innerHTML = `{"details":${response.details}, "status": ${response.status}}`;
                        
                }
            });
        })
 
    });
 
});