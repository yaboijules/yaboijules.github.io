function sendOrder() {
            var doughSize=document.getElementById("size").value;
            console.log(doughSize);
            var specialReq=document.getElementById("comments").value;
            console.log(specialReq);
            
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
            console.log(toppings);
            console.log(toppingsNum);
            
            var sizeCost = parseInt(document.getElementById('size').value)
            var numOfDrinks = parseInt(document.getElementById('drink').value)
            var numOfDeserts =  parseInt(document.getElementById('desert').value)
            
            var total = sizeCost + numOfDrinks*1 + numOfDeserts*3 +toppingsNum*.5
            
            var userName=document.getElementById("first_name").value + " " + document.getElementById("last_name").value;
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
                listtext = "You have been added to our email list. ";
            } else {
                listtext = "";
            }
            
            var address = document.getElementById('address').value
            
            document.getElementById('orderconf').innerHTML = "Hello "+userName+", thank you for your order. "+listtext+ "We will contact you at "+userEmail+" or "+phoneNumber+". Your order will cost $"+total+". Your order will be delivered to "+address+". Today is "+Date()+"."
            
            
        }