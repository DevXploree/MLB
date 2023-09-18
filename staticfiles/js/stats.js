// Game data related code
const date_game_data_today = () => {
  const today = new Date();
   // Get the element that displays the month
   const currentMonthElement = document.getElementById('current-month');

   // Get the current date
   const currentDate = new Date();

   
   document.getElementById('proceedBtn').addEventListener('click', function() {
    document.getElementById('secondPageLink').click();
});
   

   // Array of month names
   const monthNames = [
       "January", "February", "March", "April", "May", "June",
       "July", "August", "September", "October", "November", "December"
   ];

   // Get the current month number (0-indexed)
   const currentMonthNumber = currentDate.getMonth();

   // Get the current month name from the array
   const currentMonthName = monthNames[currentMonthNumber];

   // Update the content of the element with the current month name
   currentMonthElement.innerHTML = `<small>${currentMonthName}</small>`;



  const weekdays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  const dayOfWeek = weekdays[today.getDay()];
  const monthName = months[today.getMonth()];
  const day = today.getDate();
  const year = today.getFullYear();

  const formattedDate = `${dayOfWeek}, ${monthName} ${day}, ${year}`;
  console.log(formattedDate);

  const ulElements = document.querySelectorAll("button[data-date]");

  ulElements.forEach((ulElement) => {
    const dataDate = ulElement.getAttribute("data-date");

    if (dataDate === formattedDate) {
      ulElement.style.display = "flex"; // Show the ul element
    } else {
      ulElement.style.display = "none"; // Hide the ul element
    }
  });

  const separator = document.querySelectorAll("div[data-date]");

  separator.forEach((separator) => {
    const dataDate = separator.getAttribute("data-date");

    if (dataDate === formattedDate) {
      separator.style.display = "block"; // Show the ul element
    } else {
      separator.style.display = "none"; // Hide the ul element
    }
  });
  console.log("today")
};

date_game_data_today();

const showNextDate = () => {
    const today = new Date();
  
    const nextDate = new Date(today);
    nextDate.setDate(today.getDate() - 1);
    const formattedDate_first = getFormattedDate(nextDate);
  
    const next_nextDate = new Date(today);
    next_nextDate.setDate(today.getDate() - 2);
    const formattedDate_second = getFormattedDate(next_nextDate);
  
    const next_next_nextDate = new Date(today);
    next_next_nextDate.setDate(today.getDate() - 3);
    const formattedDate_3rd = getFormattedDate(next_next_nextDate);
  
    const next_next_next_nextDate = new Date(today);
    next_next_next_nextDate.setDate(today.getDate() - 4);
    const formattedDate_4th = getFormattedDate(next_next_next_nextDate);
  
    let next = document.getElementById("next");
    let next_next = document.getElementById("next-next");
    let next_next_next = document.getElementById("next-next-next");
    let next_next_next_next = document.getElementById("next-next-next-next");
  
    setListItemData(next, formattedDate_first);
    setListItemData(next_next, formattedDate_second);
    setListItemData(next_next_next, formattedDate_3rd);
    setListItemData(next_next_next_next, formattedDate_4th);
  };
  
  const getFormattedDate = (date) => {
    const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  
    const dayOfWeek = weekdays[date.getDay()];
    const monthName = months[date.getMonth()];
    const day = date.getDate();
    const year = date.getFullYear();
  
    return `${dayOfWeek}, ${monthName} ${day}, ${year}`;
  };
  
  const setListItemData = (element, formattedDate) => {
    const dateParts = formattedDate.split(" ");
    const day = dateParts[dateParts.length - 2]; // Extract the day part
    const day_without_comma = day.substring(0, day.length - 1);
    element.innerText = day_without_comma;
    element.setAttribute("value", formattedDate);
  };
  
  showNextDate();


  function isInvalidDateFormat(input) {
    // Regular expression to validate "YYYY-MM-DD" format
    const regex = /^\d{4}-\d{2}-\d{2}$/;
    return regex.test(input);
  }

  const date_game_data_onclick = (btn) => {
    let date = btn.value;

    //Formatting the data

    if(isInvalidDateFormat(date)){
        const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    
        const dateObj = new Date(date); // Convert the date string to a Date object
        const dayOfWeek = weekdays[dateObj.getDay()];
        const monthName = months[dateObj.getMonth()];
        const day = dateObj.getDate();
        const year = dateObj.getFullYear();
    
        date = `${dayOfWeek}, ${monthName} ${day}, ${year}`;
    }

    // let matches = document.getElementById("matches");
    // matches.innerHTML = "<h1>No Data found for this date</h1>";
    const ulElements = document.querySelectorAll("button[data-date]");
  
    ulElements.forEach((ulElement) => {
      const dataDate = ulElement.getAttribute("data-date");
  
      if (dataDate === date) {
        ulElement.style.display = "flex"; // Show the ul element
      } else {
        ulElement.style.display = "none"; // Hide the ul element
      }
    });
  
    const separator = document.querySelectorAll("div[data-date]");
  
    separator.forEach((separator) => {
      const dataDate = separator.getAttribute("data-date");
  
      if (dataDate === date) {
        separator.style.display = "block"; // Show the ul element
      } else {
        separator.style.display = "none"; // Hide the ul element
      }
    });

  };



  //Stats Display
  function showStats() {
    // Hide the right-body and results divs
    // Show the stats div
    const statsDiv = document.getElementById('stats-content');
    const rightBody = document.querySelector('.right-body');
    const resultsDiv = document.querySelector('.results');
    const predict = document.getElementById('predict');
    if(rightBody.style.display != 'none' || resultsDiv.style.display != 'none' || predict.style.display != "none"){
      rightBody.style.display = 'none';
      resultsDiv.style.display = 'none';
      predict.style.display = "none";
      statsDiv.style.display = 'block';
    }
}
  //Stats Display
  function showMatchup() {
    // Hide the right-body and results divs
    const statsDiv = document.getElementById('stats-content');
    const rightBody = document.querySelector('.right-body');
    const resultsDiv = document.querySelector('.results');
    const predict = document.getElementById('predict');
    if(rightBody.style.display == 'none' || resultsDiv.style.display == 'none' || predict.style.display != "none"){
      rightBody.style.display = 'flex';
      resultsDiv.style.display = 'block';
      statsDiv.style.display = 'none';
      predict.style.display = 'none';
    }
}
  //Stats Display
  function showPredict() {
    // Hide the right-body and results divs
    const predict = document.getElementById('predict');
    const statsDiv = document.getElementById('stats-content');
    const rightBody = document.querySelector('.right-body');
    const resultsDiv = document.querySelector('.results');
    if(rightBody.style.display != 'none' || resultsDiv.style.display != 'none' || statsDiv.style.display != 'none'){
      rightBody.style.display = 'none';
      resultsDiv.style.display = 'none';
      statsDiv.style.display = 'none';
      predict.style.display = 'block';
    }
}

const ranges = document.querySelectorAll('input[type="range"]');
    
    ranges.forEach(range => {
      range.min = 0;
      range.max = 100;
      range.value = 0;
      
      const valueElement = range.nextElementSibling;
      valueElement.textContent = range.value;
      
      range.addEventListener('input', () => {
        valueElement.textContent = range.value;
      });
    });

    var team1Value = document.querySelector('input[name="team1"]').value
    var team2Value = document.querySelector('input[name="team2"]').value
    let team1 = document.getElementById("team1h1");
    let team2 = document.getElementById("team2h1");
    console.log(team1)
    var proceedButton = document.getElementById("proceedBtn")

    function updateButton() {
      console.log("hi i am update function")
      if (team1.innerText != "" && team2.innerText != "") {
        proceedButton.removeAttribute("disabled")
      } else {
        proceedButton.setAttribute("disabled", "disabled");
      }
    }

    updateButton()

    // document.querySelector('input[name="team1"]').addEventListener("input", function () {
    //   team1Value = this.value;
    //   updateButton();
    // });
  
    // document.querySelector('input[name="team2"]').addEventListener("input", function () {
    //   team2Value = this.value;
    //   updateButton();
    // });
  
