function emailList() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    if (name.length == 0) {
        alert('Please enter your name!');
    }
    if (email.length == 0) {
        alert('Please enter your email!');
    }
    if (email.length>0 && name.length>0) {
        alert('Thank you, you have been added to our mailing list!')
    }
}

    function bookTrip() {
                var name = document.getElementById('firstname').value + ' ' + document.getElementById('lastname').value;
                if(name.length<2){
                    alert('Please enter your name.');
                    return;
                }
                
                var arrivals = document.getElementsByName('arrival');
                for(var i=0;i<arrivals.length;i++){
                    if(arrivals[i].checked){
                        var arrival = parseInt(arrivals[i].value);
                        break;
                    }
                }
                console.log(arrival);
                
                var hotels = document.getElementsByName('hotel');
                for(i=0;i<hotels.length;i++){
                    if(hotels[i].checked){
                        var hotel = parseInt(hotels[i].value);
                        break;
                    }
                }
                console.log(hotel);
                
                var travelers = parseInt(document.getElementById('people').value);
                console.log(travelers);
                
                var days = parseInt(document.getElementById('days').value);
                console.log(days);
                
                var extra = 0
                if(document.getElementById('wifi').checked){
                    extra += 10;
                }
                if(document.getElementById('recline').checked) {
                    extra += 20;
                }
                console.log(extra);
                
                var meals = document.getElementsByName('food');
                for(i=0;i<meals.length;i++){
                    if(meals[i].checked) {
                        var meal = parseInt(meals[i].value);
                        break;
                    }
                }
                console.log(meal);

                var total = (arrival*travelers)+(hotel*days)+(extra*travelers)+(meal*travelers);
                console.log(total);
                
                document.getElementById('total').innerHTML = "Thank you " + name + ". Your total is $"+total;
            }