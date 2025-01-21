import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const Results = ({ data }) => {
    return (
        <div style={styles.container}>
            <Navbar />
            <main style={styles.mainContent}>
                <h1 style={styles.title}>Analysis Results</h1>
                {data && data.length > 0 ? (
                    <div style={styles.resultsContainer}>
                        {data.map((result, index) => (
                            <div key={index} style={styles.resultItem}>
                                <h3>{result.title}</h3>
                                <p>{result.description}</p>
                                {result.issues && result.issues.length > 0 && (
                                    <ul>
                                        {result.issues.map((issue, idx) => (
                                            <li key={idx}>{issue}</li>
                                        ))}
                                    </ul>
                                )}
                            </div>
                        ))}
                    </div>
                ) : (
                    <p style={styles.noData}>No results available. Please run an analysis.</p>
                )}
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
    resultsContainer: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '20px',
    },
    resultItem: {
        border: '1px solid #ccc',
        borderRadius: '5px',
        padding: '15px',
        maxWidth: '600px',
        width: '100%',
        textAlign: 'left',
        backgroundColor: '#f9f9f9',
    },
    noData: {
        fontSize: '1.2em',
        color: '#666',
    },
};

export default Results;
