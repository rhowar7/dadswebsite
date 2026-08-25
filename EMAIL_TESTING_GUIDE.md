# Email Testing Instructions for Estimate Form

## Manual Testing Steps

### Step 1: Open the Estimate Form
1. Open `estimate.html` in your web browser
2. Make sure you're connected to the internet

### Step 2: Fill Out the Form
Use these test values:
- **Full Name**: Test User
- **Phone Number**: (443) 829-5946
- **Email Address**: test@example.com
- **Property Address**: 123 Test Street, Test City, MD 21084
- **Type of Work Needed**: Kitchen Remodel (or Bathroom Remodel)
- **Project Description**: This is a test submission to verify email functionality
- **Preferred Timeline**: As soon as possible

### Step 3: Submit the Form
1. Click "Submit Estimate Request →"
2. Watch for the green success message to appear (the form hides after a successful send)
3. Optional: open the browser console (F12) if something looks wrong

### Step 4: Verify Email Receipt
1. Check your Gmail inbox at whoward45@gmail.com
2. Look for an email from EmailJS with subject line containing the form data
3. If no email arrives within 5-10 minutes, check your spam folder

## Debugging Steps

### Check Browser Console
1. Press F12 to open developer tools
2. Go to the Console tab
3. Submit the form
4. Look for these messages:
   - "Form submitted" (validation passed)
   - "Validation passed, sending email..." (form is valid)
   - "Template params: [object]" (email parameters prepared)
   - "Email sent successfully!" (email sent)
   - OR error messages if something fails

### Common Issues & Solutions

#### Issue: Success message doesn't appear
**Solution**: Check console for JavaScript errors. The form now has fallback success messages.

#### Issue: Email doesn't arrive
**Possible causes**:
1. EmailJS service down (check https://www.emailjs.com/)
2. API keys expired (need to renew EmailJS account)
3. Email marked as spam
4. Network connectivity issues

#### Issue: Form validation fails
**Solution**: Make sure all required fields (*) are filled out completely.

## Alternative Testing Methods

### Method 1: Use Browser Developer Tools
1. Open estimate.html
2. Press F12 → Network tab
3. Fill and submit form
4. Look for EmailJS network requests

### Method 2: Test EmailJS Directly
Create a simple test HTML file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>EmailJS Test</title>
</head>
<body>
    <button onclick="testEmail()">Test Email</button>
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/index.min.js"></script>
    <script>
        emailjs.init('9_j-uvK3QR4l9VL-C');

        function testEmail() {
            emailjs.send('service_5mxrcrc', 'template_puxk7oa', {
                to_email: 'whoward45@gmail.com',
                from_name: 'Test User',
                from_email: 'test@example.com',
                phone: '(443) 829-5946',
                address: '123 Test St',
                work_type: 'Test',
                description: 'Testing EmailJS functionality',
                timeline: 'ASAP'
            }).then(function(response) {
                console.log('SUCCESS!', response);
                alert('Email sent successfully!');
            }, function(error) {
                console.log('FAILED...', error);
                alert('Email failed: ' + JSON.stringify(error));
            });
        }
    </script>
</body>
</html>
```

### Method 3: Check EmailJS Dashboard
1. Go to https://www.emailjs.com/
2. Log into your account
3. Check the service and template status
4. View sent emails log

## Expected Email Content

When working correctly, you should receive an email with:
- **From**: EmailJS service
- **Subject**: Based on your EmailJS template
- **Content**: All form fields (name, phone, email, address, work type, description, timeline)

## If Emails Still Don't Work

1. **Check EmailJS Account Status**: Ensure your account is active and has credits
2. **Verify API Keys**: Make sure the service ID and template ID are correct
3. **Contact EmailJS Support**: If service issues persist
4. **Alternative Solution**: Consider switching to a different email service like Formspree, Netlify Forms, or a backend solution

---

**Test Result**: [ ] Email received successfully
**Test Date**: [ ]
**Notes**: [ ]