import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import App from '../App';

// Mock components
jest.mock('../pages/Home', () => () => <div>Home Page</div>);
jest.mock('../pages/Results', () => () => <div>Results Page</div>);

describe('App Component', () => {
    test('renders Home page by default', () => {
        render(
            <Router>
                <App />
            </Router>
        );
        expect(screen.getByText(/Home Page/i)).toBeInTheDocument();
    });

    test('renders Results page when path is /results', () => {
        window.history.pushState({}, 'Results Test', '/results');

        render(
            <Router>
                <App />
            </Router>
        );
        expect(screen.getByText(/Results Page/i)).toBeInTheDocument();
    });
});
