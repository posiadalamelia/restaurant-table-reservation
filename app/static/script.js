const tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate() + 1);
const tomorrowDate = tomorrow.toISOString().split('T')[0];
document.getElementById('date').setAttribute('min', tomorrowDate);

function setTimeRange()
        {
            const timeInput = document.getElementById("time")
            const now = new Date();
            const minTime="09:00";
            const maxTime="18:00";
            timeInput.min = minTime;
            timeInput.max = maxTime;
        }
        window.onload = setTimeRange;