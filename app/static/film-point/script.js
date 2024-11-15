document.querySelector('.spark-button').addEventListener('mousemove', function (e) {
    const button = e.currentTarget;

    // Create multiple sparks when mouse moves over the button
    for (let i = 0; i < 100; i++) {  // You can change the number of sparks here
        const spark = document.createElement('div');
        spark.classList.add('spark');

        // Randomly position each spark around the mouse position
        const offsetX = Math.random() * button.offsetWidth;
        const offsetY = Math.random() * button.offsetHeight;

        // Position sparks based on mouse coordinates
        spark.style.left = `${e.offsetX + offsetX - button.offsetWidth / 2}px`;
        spark.style.top = `${e.offsetY + offsetY - button.offsetHeight / 2}px`;

        button.appendChild(spark);

        // Remove the spark element after animation
        setTimeout((500) => {
            spark.remove();
        }, 500); // Time should match the duration of the animation
    }
});
