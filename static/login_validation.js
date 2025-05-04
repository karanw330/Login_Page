function Validation() {
  let username = document.getElementById("exampleFormControlInput1").value.trim();
  let password = document.getElementById("exampleFormControlInput2").value.trim();

  let username_border = "";
  let password_border = "";
  let usernameError = "";
  let passwordError = "";

  if (username.length === 0) {
    usernameError = "Cannot leave a blank entry";
    username_border = "1px solid red";
  } else if (username.length < 5) {
    usernameError = "Username is too short";
    username_border = "1px solid red";
  }

  if (password.length === 0) {
    passwordError = "Cannot leave a blank entry";
    password_border = "1px solid red";
  } else if (password.length < 8) {
    passwordError = "Minimum 8 characters are required in password";
    password_border = "1px solid red";
  }

  document.getElementById("username-error").innerHTML = usernameError;
  document.getElementById("password-error").innerHTML = passwordError;
  document.getElementById("exampleFormControlInput1").style.border = username_border;
  document.getElementById("exampleFormControlInput2").style.border = password_border;



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
        document.getElementById("exampleFormControlInput2").style.border = "1px solid red";
      } else if (data.confirmation === "DNE") {
        document.getElementById("username-error").innerHTML = "User does not exist. Please register.";
        document.getElementById("exampleFormControlInput1").style.border = "1px solid red";
      } else {
        alert("Unexpected error. Please try again.");
      }
    })

  }
}