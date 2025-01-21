import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const Home = () => {
    return (
        <div style={styles.container}>
            <Navbar />
            <main style={styles.mainContent}>
                <h1 style={styles.title}>Welcome to AIris AI</h1>
                <p style={styles.description}>
                    AIris AI helps you detect potential scams and rug pulls in the cryptocurrency space.
                    Analyze smart contracts, monitor wallet activity, and more with cutting-edge AI technology.
                </p>
                <button style={styles.button} onClick={() => alert('Get Started!')}>
                    Get Started
                </button>
            </main>
            <Footer />
        </div>
    );
};

const styles = {
    container: {
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
    },
    mainContent: {
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        padding: '20px',
    },
    title: {
        fontSize: '2.5em',
        fontWeight: 'bold',
        marginBottom: '20px',
    },
    description: {
        fontSize: '1.2em',
        marginBottom: '30px',
        maxWidth: '600px',
    },
    button: {
        padding: '10px 20px',
        fontSize: '1em',
        backgroundColor: '#61dafb',
        color: '#fff',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
    },
};

export default Home;
