export function errorStatus(errors) {
    let statusModal = $('#status')
    let html = '';
    for (const error of errors) 
        html += `<p class="text-danger">${error}</p>`;
    statusModal.find('.modal-body').html(html);
    const modal = bootstrap.Modal.getOrCreateInstance(statusModal);
    modal.show();
}

export function successStatus(messages) {
    let statusModal = $('#status')
    let html = '';
    for (const message of messages) 
        html += `<p class="text-success">${message}</p>`;
    statusModal.find('.modal-body').html(html);
    const modal = bootstrap.Modal.getOrCreateInstance(statusModal);
    modal.show();
}