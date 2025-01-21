import React from 'react';

const Footer = () => {
    return (
        <footer style={styles.footer}>
            <div style={styles.text}>
                &copy; {new Date().getFullYear()} AIris AI. All rights reserved.
            </div>
            <div style={styles.links}>
                <a href="/privacy" style={styles.link}>Privacy Policy</a>
                <a href="/terms" style={styles.link}>Terms of Service</a>
            </div>
        </footer>
    );
};

const styles = {
    footer: {
        backgroundColor: '#282c34',
        color: '#fff',
        textAlign: 'center',
        padding: '10px 20px',
        marginTop: 'auto',
    },
    text: {
        marginBottom: '10px',
    },
    links: {
        display: 'flex',
        justifyContent: 'center',
        gap: '15px',
    },
    link: {
        color: '#61dafb',
        textDecoration: 'none',
    },
};

export default Footer;
