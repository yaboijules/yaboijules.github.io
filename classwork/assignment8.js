function sendOrder() {
            //i created an empty array and the id of every checked box gets added to the array using var.push()
            var toppingslist=document.getElementsByName("toppings");
            var toppings=[]
            var toppingsNum = 0;
            for(var i=0;i<toppingslist.length;i++) {
                if (toppingslist[i].checked) {
                    toppings.push(toppingslist[i].id);
                    toppingsNum++
                }
            }
            
            var sizeCost = parseInt(document.getElementById('size').value)
            var sizeName 
            switch(sizeCost) {
                case 6: 
                    sizeName = 'small'; 
                    break; 
                case 9: 
                    sizeName = 'medium'; 
                    break; 
                case 12: 
                    sizeName = 'large'; 
                    break; 
                case 16: 
                    sizeName = 'extra large'; 
                    break;
            }
            
            var specialReq=document.getElementById("comments").value;
    
            var numOfDrinks = parseInt(document.getElementById('drink').value)
            var numOfDeserts =  parseInt(document.getElementById('desert').value)
            
            var total = sizeCost + numOfDrinks*1 + numOfDeserts*3 +toppingsNum*.5
            if(isNaN(total)){
                alert('Please select a pizza size!');
                return;
            }
            
            var bonus
            if (total >= 25) {
                bonus = "You've earned a free medium pizza with your next order! The code is Q1358.<br>";
            } else {
                bonus = "";
            };
            
            var userName=document.getElementById("name").value;
            var phoneNumber=document.getElementById("phone_num").value;
            var userEmail=document.getElementById('email').value;
            
            var yesornolist = document.getElementsByName("ad_list");
            var yesorno
            for(var i=0;i<yesornolist.length;i++) {
                if (yesornolist[i].checked){
                    yesorno=yesornolist[i].value;
                }
            }
            var listtext
            if (yesorno==="yes") {
                listtext = "You have been added to our email list.<br>";
            } else {
                listtext = "";
            }
            
            var address = document.getElementById('address').value
            
            if(userName.length<1||phoneNumber.length<1||userEmail.length<1||address.length<1){
                alert('Please fill in all required data.');
                return;
            }
            
            var d = new Date();
            var orderDate = `${d.getMonth()}/${d.getDate()}/${d.getFullYear()}`;
            
            function getTime() {
                var hour = d.getHours();
                var ampm = 'am'
                if (hour >= 12) {
                    ampm = 'pm';
                    hour -=12;
                }
                if (hour == 0) {
                    hour = 12;
                }
                var minute = d.getMinutes();
                if (minute<10){
                    minute = "0" + minute;
                }
                var seconds = d.getSeconds();
                if (seconds<10){
                    seconds = "0" + seconds;
                }
                return `${hour}:${minute}:${seconds} ${ampm}`
            }
    
            var orderTime = getTime();
            
            document.getElementById('orderconf').innerHTML = `Thank you for your order ${userName}.<br>Your pizza will be delivered to ${address}.<br>Your phone number is ${phoneNumber}.<br>${listtext}You ordered a ${sizeName} ${toppingsNum} topping pizza<br> with these toppings: ${toppings}<br>You ordered ${numOfDrinks} drinks.<br> You ordered ${numOfDeserts} deserts.<br> Special instructions are: ${specialReq}<br>Total cost is $${total}.<br>${bonus}Your order was placed on ${orderDate} at ${orderTime}.`
            
            
        }