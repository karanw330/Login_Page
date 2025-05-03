function Validation() {
  let username = document.getElementById("exampleFormControlInput1").value.trim();
  let password = document.getElementById("exampleFormControlInput2").value.trim();

  let usernameError = "";
  let passwordError = "";

  if (username.length === 0) {
    usernameError = "Cannot leave a blank entry";
  } else if (username.length < 5) {
    usernameError = "Username is too short";
  }

  if (password.length === 0) {
    passwordError = "Cannot leave a blank entry";
  } else if (password.length < 8) {
    passwordError = "Minimum 8 characters are required in password";
  }

  document.getElementById("username-error").innerHTML = usernameError;
  document.getElementById("password-error").innerHTML = passwordError;

  if (usernameError === "" && passwordError === "") {
    fetch("/authentication", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
    })
    .then(response => response.json())
    .then(data => {
      if (data.confirmation === "OK") {
        window.location.href = "/Dashboard";
      } else if (data.confirmation === "NO") {
        document.getElementById("password-error").innerHTML = "Incorrect password";
      } else if (data.confirmation === "DNE") {
        document.getElementById("username-error").innerHTML = "User does not exist. Please register.";
      } else {
        alert("Unexpected error. Please try again.");
      }
    })

  }
}