<template>
    <button type="button"
        :class="disabled ? 
        'items-center justify-center mx-8 my-3 text-sm font-bold text-center text-primary-700 underline hover:text-primary-800 rounded-lg cursor-not-allowed' :
        'items-center justify-center mx-8 my-3 text-sm font-bold text-center text-primary-700 underline hover:text-primary-800 rounded-lg'"
        :disabled="disabled">
        {{ text }}
        <slot />
    </button>
</template>
<script>
export default {
    props: {
        text: String,
        disabled: false
    }
}
</script>
