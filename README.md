# Advanced Calculator App

A beautiful, modern calculator application built with React frontend and Flask backend, featuring advanced animations and an EMI calculator.

## 🚀 Features

### Calculator
- **Modern UI**: Clean, responsive design with glass-morphism effects
- **Smooth Animations**: Powered by Framer Motion for delightful interactions
- **Full Functionality**: Addition, subtraction, multiplication, division, parentheses
- **Keyboard Support**: Use your keyboard for quick calculations
- **Error Handling**: Graceful handling of invalid expressions and division by zero
- **Real-time Display**: Shows both expression and result simultaneously

### EMI Calculator
- **Loan Calculations**: Calculate monthly EMI, total interest, and total amount
- **Input Validation**: Real-time validation with helpful error messages
- **Beautiful Results**: Animated results display with currency formatting
- **Responsive Design**: Works perfectly on all devices

## 🛠️ Tech Stack

### Frontend
- **React 18**: Modern React with hooks
- **Framer Motion**: Smooth animations and transitions
- **Styled Components**: CSS-in-JS for component styling
- **Lucide React**: Beautiful icons
- **Axios**: HTTP client for API calls

### Backend
- **Flask**: Python web framework
- **Flask-CORS**: Cross-origin resource sharing
- **Python**: Core calculation logic

## 📦 Installation

### Prerequisites
- Node.js (v14 or higher)
- Python 3.7+
- npm or yarn

### Backend Setup
1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask backend:
```bash
python app.py
```

The backend will be available at `http://localhost:5000`

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## 🎯 Usage

### Calculator
- Click buttons or use keyboard for input
- Supports all basic arithmetic operations
- Use parentheses for complex expressions
- Press Enter or = to calculate
- Press Escape to clear
- Press Backspace to delete last character

### EMI Calculator
- Enter loan amount, interest rate, and tenure
- Click "Calculate EMI" to see results
- View detailed breakdown including:
  - Monthly EMI
  - Principal Amount
  - Total Interest
  - Total Amount

## 🎨 UI Features

- **Glass-morphism Design**: Modern translucent effects
- **Gradient Backgrounds**: Beautiful color transitions
- **Smooth Animations**: Page transitions and button interactions
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Dark/Light Theme**: Automatic theme detection
- **Loading States**: Visual feedback during calculations
- **Error Handling**: User-friendly error messages

## 🔧 Development

### Project Structure
```
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── frontend/             # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Calculator.js
│   │   │   └── EMICalculator.js
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
└── README.md
```

### Available Scripts

**Backend:**
- `python app.py` - Start Flask development server

**Frontend:**
- `npm start` - Start React development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm eject` - Eject from Create React App

## 🌟 Advanced Features

### Animations
- **Page Transitions**: Smooth tab switching
- **Button Interactions**: Hover and click animations
- **Loading States**: Animated calculation feedback
- **Error Messages**: Smooth error display
- **Results Display**: Animated results appearance

### User Experience
- **Keyboard Navigation**: Full keyboard support
- **Input Validation**: Real-time validation
- **Error Recovery**: Graceful error handling
- **Responsive Design**: Mobile-first approach
- **Accessibility**: ARIA labels and keyboard support

## 🚀 Deployment

### Backend Deployment
The Flask app can be deployed to:
- Heroku
- PythonAnywhere
- AWS
- Google Cloud Platform

### Frontend Deployment
The React app can be deployed to:
- Vercel
- Netlify
- GitHub Pages
- AWS S3

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Framer Motion for animations
- Lucide for beautiful icons
- Styled Components for styling
- Flask for the backend framework 