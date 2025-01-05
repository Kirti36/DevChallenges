const eZsnippet = () => {
    try {
        throw new Error('error');
    } catch (error) {
        return 'inside error';
    } finally {
        return 'outside error';
    }
};