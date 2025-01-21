import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Results from './pages/Results';

const App = () => {
    const dummyData = [
        {
            title: "Smart Contract Analysis",
            description: "Analyzed a contract with potential vulnerabilities.",
            issues: ["Use of selfdestruct", "Use of tx.origin"]
        },
        {
            title: "Wallet Monitoring",
            description: "Suspicious wallet activity detected.",
            issues: ["Unusually large transfer", "Rapid sequential transactions detected"]
        }
    ];

    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/results" element={<Results data={dummyData} />} />
            </Routes>
        </Router>
    );
};

export default App;
