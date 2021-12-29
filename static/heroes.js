function getEdit() {
    const appearance = {
        gender: $('#gender').val(),
        race: $('#race').val(),
        eye_colour: $('#eye_colour').val(),
        hair_colour: $('#hair_colour').val(),
    };

    const biography = {
        full_name: $('#full_name').val(),
        place_of_birth: $('#place_of_birth').val(),
        alignment: $('#alignment').val(),
        occupation: $('#occupation').val(),
    };

    return {
        name: $('#name').val(),
        appearance: appearance,
        biography: biography,
    };
}

function createHero() {
    $.ajax(`/api/heroes`, {
        data: JSON.stringify(getEdit()),
        dataType: 'JSON',
        method: 'POST',
        contentType: 'application/json'
    }).done(() => {
        window.location.href = '/heroes'
    });
}

function editHero(heroId) {
    $.ajax(`/api/heroes/${heroId}`, {
        data: JSON.stringify(getEdit()),
        dataType: 'JSON',
        method: 'PUT',
        contentType: 'application/json'
    }).done(() => {
        window.location.href = '/heroes'
    });
}

function deleteHero(heroId) {
    $.ajax(`/api/heroes/${heroId}`, {
        method: 'DELETE'
    }).done(() => {
       window.location.href = '/heroes';
    });
}