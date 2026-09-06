using System;

namespace UserLogin
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void OnLoginClicked(object sender, EventArgs e)
        {
            // Retrieve input values
            string userId = UserIdEntry.Text?.Trim();
            string password = PasswordEntry.Text?.Trim();

            // Check credentials
            if (userId == "Johnson" && password == "Password1")
            {
                // Display success message
                StatusLabel.Text = $"Login successful!! Welcome, {userId}.";
                StatusLabel.TextColor = Colors.Green;
            }
            else
            {
                // Display failure message
                StatusLabel.Text = $"Login failed. User ID entered: {userId}";
                StatusLabel.TextColor = Colors.Red;
            }
        }

        private void OnCancelClicked(object sender, EventArgs e)
        {
            // Clear input fields and status message
            UserIdEntry.Text = string.Empty;
            PasswordEntry.Text = string.Empty;
            StatusLabel.Text = string.Empty;
        }
    }
}