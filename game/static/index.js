function startTime() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('txt').innerHTML ="Time:" + h + ":" + m + ":" + s;
  setTimeout(startTime, 1000);
}

function checkTime(i) {
  if (i < 10) {i = "0" + i}  // add zero in front of numbers < 10
  return i;
}


// // ACtual TIME HERE
// // Set the date we're counting down to
// var countDownDate = new Date("Jan 5, 2024 15:37:25").getTime();
//
// // Update the count down every 1 second
// var x = setInterval(function() {
//
//   // Get today's date and time
//   var now = new Date().getTime();
//
//   // Find the distance between now and the count down date
//   var distance = countDownDate - now;
//
//   // Time calculations for days, hours, minutes and seconds
//   var days = Math.floor(distance / (1000 * 60 * 60 * 24));
//   var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//   var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//   var seconds = Math.floor((distance % (1000 * 60)) / 1000);
//
//   // Display the result in the element with id="demo"
//   document.getElementById("demo").innerHTML = days + "d " + hours + "h "
//   + minutes + "m " + seconds + "s ";
//
//   // If the count down is finished, write some text
//   if (distance < 0) {
//     clearInterval(x);
//     document.getElementById("demo").innerHTML = "EXPIRED";
//   }
// }, 1000);
//
//
//
// // sec
//
(function countdown(remaining) {
    if(remaining <= 0)
        location.reload(true);
    document.getElementById('countdown').innerHTML = "DEI";
    setTimeout(function (){ countdown(remaining - 1); }, 1000);
})(10); // 5 seconds
//
//
// // end
//
// const span = document.getElementById('countdown')
//
// const deadline = new Date
// deadline.setHours(0)
// deadline.setMinutes(0)
// deadline.setSeconds(0)
//
// function displayRemainingTime() {
//   if (deadline < new Date) deadline.setDate(deadline.getDate() + 1)
//   const remainingTime = deadline - new Date
//   const extract = (maximum, factor) => Math.floor((remainingTime % maximum) / factor)
//   const seconds = extract(   60000, 1000   )
//   const minutes = extract( 3600000, 60000  )
//   const hours   = extract(86400000, 3600000)
//   const string = `${hours} hours ${minutes} minutes ${seconds} seconds remaining`
//   span.innerText = `${hours} hours ${minutes} minutes ${seconds} seconds remaining`
// }
// window.setInterval(displayRemainingTime, 1000)
// displayRemainingTime()
//
//
//


