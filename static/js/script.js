document.addEventListener('DOMContentLoaded', function() {
    var timeLimit = 60; // 1 minute
    var timer = setInterval(function() {
        var minutes = Math.floor(timeLimit / 60);
        var seconds = timeLimit % 60;
        document.getElementById('timer').innerHTML = "Time remaining: " + minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
        timeLimit--;
        if (timeLimit < 0) {
            clearInterval(timer);
            document.getElementById('quizForm').submit(); // Ensure this ID matches the form ID in your HTML
        }
    }, 1000);
});
